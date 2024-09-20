//fix the errors and complete the code.

const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');


function handleInput(command) {


    switch (action) {

        case 'help':
            viewCommand();
            break;

        default:
            terminalOutput.textContent += `Invalid command: ${command}\n`;
            break;
    }

    terminalInput.value = '';
}

function viewCommand() {
    terminalOutput.innerHTML += "Available Commands:"

}



