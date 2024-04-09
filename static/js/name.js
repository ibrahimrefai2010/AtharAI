function CallPythonSetName() { //sends the user's name to the frontend using AJAX the name is passed through the disered route, the name through the url itslef for example /setname/ibrahim 
    let name = document.getElementById('name_input').value;
    window.location.replace("/loading");
    console.log(name)
    $.ajax({
        type: 'POST',
        url: `/setname/${name}`,
        data: {},  // Pass data to Python function
        success: function(response) {
            window.location.replace("/chat");
            console.log('Python function executed:', response);
        },
        error: function(error) {
            console.error('Error calling Python function:', error);
        }
    });
}
