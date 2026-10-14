from pyscript import display, document

def student_club(e):
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    candidate_name = f"{first_name} {last_name}"

    club_members = [ 'Sponge squarepants','Maria Toes','Ladis my ahh','Ana elsa', 'John Jack']

    member_checker = candidate_name in club_members

    display_message = (f"Sorry {candidate_name},your name is not on the list.", f"Congratulations {candidate_name}! You are now part of the ICT club." )

    result = document.getElementById('result')
    result.innerHTML = ""

    display(display_message[member_checker], target='result')