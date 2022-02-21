
import Asym

# Read the encrypted message from "message_test.enc"
# Read Keys file from "sample_test.keys"   File format is similar to the previous tutorial
# Check and print who is the receiver of this message

if __name__ == '__main__':
    print('This message is for .... ')
    keys = Asym.load_keys('samples_test.keys')
    Asym.decrypt_message(keys)
