import pyorient
from time import time
import random
import numpy
from tqdm import tqdm
import csv
import string
import bcrypt

# Constants
db_name = 'particulate-matter-main'
user_count = 1000
current_millis = int(time() * 1000)
first_names_male = ["Jonas", "Emil", "Linus", "Lukas", "Thomas", "Felix", "Alexander", "Paul", "Elias", "Liam", "Theo", "Anton", "Markus"]
first_names_female = ["Laura", "Emilia", "Anna", "Julia", "Ella", "Lina", "Lena", "Leonie", "Sarah", "Ida"]
last_names = ["Müller", "Schmidt", "Schneider", "Fischer", "Meyer", "Weber", "Hofmann", "Wagner", "Becker", "Schulz", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Schröder", "Wolf"]
email_providers = ["gmail.com", "gmx.com", "web.de", "outlook.com", "yahoo.com", "mail.com", "webmail.de", "aol.com", "icloud.com", "sap.com", "chillibits.com"]

# --------------------------------------------------------------------------------------------------- Functions ---------------------------------------------------------------------------------------------------

def get_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

# -------------------------------------------------------------------------------------------------- Main Program -------------------------------------------------------------------------------------------------

# Initialize database connection
client = pyorient.OrientDB('localhost', 2424)
session_id = client.connect('root', 'root')

# Prepare database
if client.db_exists(db_name, pyorient.STORAGE_TYPE_PLOCAL):
    client.db_drop(db_name)
client.db_create(db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_PLOCAL)

# Create Sensor class
print("Importing sensors ...")
client.command('create class Sensor extends V')
# Import sensors from csv file
sensor_count = 1
with open('sensors.csv', 'r', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in tqdm(reader):
        # Extract data fields
        chip_id = row['chip_id']
        firmware_version = row['firmware_version']
        creation_date = row['creation_date']
        notes = ''  # Had to be anonymized
        last_update = row['last_update']
        last_edit = row['last_edit']
        lat = row['lat']
        lng = row['lng']
        alt = row['alt']
        country = row['country']
        city = row['city']
        maps_url = row['maps_url']
        last_value = row['last_value']
        last_value_2 = row['last_value_2']
        # Push record into the OrientDB
        query = f'insert into Sensor set id = {sensor_count}, chip_id = {chip_id}, firmware_version = "{firmware_version}", creation_date = {creation_date}, notes = "{notes}", last_update = {last_update}, last_edit = {last_edit}, lat = {lat}, lng = {lng}, alt = {alt}, country = "{country}", city = "{city}", maps_url = "{maps_url}", last_value = {last_value}, last_value_2 = {last_value_2}'
        client.command(query)
        sensor_count += 1

# Create User class
print("Generating users ...")
client.command('create class User extends V')
# Generate demo users
for id in tqdm(range(1, user_count +1)):
    # Generate first name
    first_name_list = first_names_female
    if random.randint(0, 1) == 0:
        first_name_list = first_names_male
    first_name = first_name_list[random.randint(0, len(first_name_list) -1)]
    # Generate last name
    last_name = last_names[random.randint(0, len(last_names) -1)]
    # Generate email
    email_provider = email_providers[random.randint(0, len(email_providers) -1)]
    email = first_name.lower() + "." + last_name.lower() + "@" + email_provider
    # Generate confirmationToken
    confirmation_token = get_random_string(20)
    # Generate random password
    password = bcrypt.hashpw(get_random_string(30).encode(), bcrypt.gensalt()).decode()
    # Generate role
    role = numpy.random.choice(numpy.arange(1, 4), p=[0.9, 0.09, 0.01])  # 1 = Normal user, 2 = Operator, 3 = Administrator
    # Generate status
    status = numpy.random.choice(numpy.arange(1, 5), p=[0.9, 0.08, 0.01, 0.01])  # 1 = active, 2 = email confirmation pending, 3 = suspended, 4 = locked
    # Generate creationTimestamp
    creation_timestamp = random.randint(1533074400000, current_millis)
    # Generate lastEditTimestamp
    last_edit_timestamp = random.randint(creation_timestamp, current_millis)
    # Push record into the OrientDB
    query = f'insert into User set id = {id}, first_name = "{first_name}", last_name = "{last_name}", email = "{email}", confirmation_token = "{confirmation_token}", password = "{password}", role = {role}, status = {status}, creation_timestamp = {creation_timestamp}, last_edit_timestamp = {last_edit_timestamp}'
    client.command(query)

# Generate links
print("Generating links ...")
client.command('create class Link extends E')
link_id = 1
# Generate demo links
for user_id in tqdm(range(1, user_count +1)):
    current_user_link_count = random.randint(0, 10)
    for i in range(1, current_user_link_count):
        # Get random sensor id
        sensor_id = random.randint(1, sensor_count -1)
        # Generate owner
        owner = random.randint(0, 1)  # Boolean - 0 = not the owner, 1 = the owner
        # Generate name
        name = "Sensor {:02d}".format(i)
        # Generate color
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0,255)
        color = red
        color = (color << 8) + green
        color = (color << 8) + blue
        # Generate creationTimestamp
        creation_timestamp = random.randint(1533074400000, current_millis)
        # Push record into the OrientDB
        query = f'create edge Link from (select from User where id = {user_id}) to (select from Sensor where id = {sensor_id}) set owner = {owner}, name = "{name}", color = {color}, creation_timestamp = {creation_timestamp}'
        client.command(query)
        link_id += 1

print("Done!")