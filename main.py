# Main Method 
import spam_detection as sd

def main():
    '''
    Main Method
    '''
    print("Welcome to the Spam Detector.")
    inputted = input("Input a Message: ")
    print("Our Spam Detection System has determined your message to be " + sd.detect(inputted))

if __name__ == '__main__':
    main()