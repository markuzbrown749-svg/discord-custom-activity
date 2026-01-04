from discoIPC import ipc
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'details': '.',
    'state' : '˚₊‧꒰ა ☆ ໒꒱ ‧₊˚',
    'assets': {
        'large_image': '633ed6f64f207049add707032d4f1d0f',
        'large_text': '‧₊˚🖇️✩ ₊˚',
        'small_image': '9be2daef9cec2cf505153955b6b69a58',
        'small_text': 'Hey Netherite Knight!!'
    },
    'party': {
        'size': [1, 5]
   }
}

def main():
    client = ipc.DiscordIPC(config['CLIENT']['client_id'])
    # Connect to Discord Client
    client.connect()

    print('\nStarting Custom Activity...\n')
    time.sleep(5)

    try:
        client.update_activity(set_activity()) # Update Activity
        while True:
            input('\nConnected! ')
            # Do nothing   

    except KeyboardInterrupt:
        print('Disconnecting...\n')
        client.disconnect()

def set_activity():
    # Set acitivty for the player.
    activity = base_activity
    return activity

if __name__ == '__main__':
    main()
