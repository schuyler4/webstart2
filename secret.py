from flask.ext.scrypt import generate_password_hash, generate_random_salt, check_password_hash
salt = generate_random_salt()