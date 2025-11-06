# function to check the string of the password
from zxcvbn import zxcvbn
from getpass import getpass

def check_strength(password):# this is a funtion used to check password strength
    result = zxcvbn(password)
    score = result['score']
    if score == 3: # score 3 which is strong enough
        response = "Strong enough password: Score of 3"
    elif score == 4: #score 4 which is very strong
        response = "Very strong password: Score of 4"
    else:
        feedback = result.get("feedback") # if not 3 or 4 then use a feedback system which gives a warning
        Warning = feedback.get("warning") #
        suggestions = feedback.get("suggestions")
        response = "week password: Score of " + str(score)
        response += "\n warning: " + Warning
        response += "\n Suggestions: "
        for suggestion in suggestions: # iterate through the suggestions
            response += " " + suggestion
            
    return response

if __name__ == "__main__":
    while True:
        password1 = getpass("Enter a password to get strength: ")   #
        print(check_strength(password1))
        if check_strength(password1).startswith("weak"):
            print ("choose a stronger password.")
        else:
            break