from pyscript import document, display

def inputUser (e):
    document.getElementById('output').innerHTML =''

    input = document.getElementById('country').value

    display(input, target='output')