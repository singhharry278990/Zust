$(document).ready(function() {
  // Handle form submission
  $('#profile-information').on('submit', '.account-setting-form', function(e) {
    e.preventDefault(); // Prevent default form submission

    // Get form data
    var formData = $(this).serialize();
    
    var occupation = $('#Occupation option:selected').text();
    var gender = $('#Gender option:selected').text();
    var relationStatus = $('#Relation_Status option:selected').text();
    var bloodGroup = $('#Blood_Group option:selected').text();
    var language = $('#language option:selected').text();
    var country = $('#country option:selected').text();

    // Create an object to hold the form data
    var dataObject = {
      occupation: occupation,
      gender: gender,
      relation_status: relationStatus,
      blood_group: bloodGroup,
      language: language,
      country: country
    };

    // Send AJAX request to Django view
    $.ajax({
      type: 'POST',
      url: '{% url "personal-info" %}', // Replace with the correct URL path to your Django view
      data: JSON.stringify(dataObject),
      contentType: 'application/json',
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      },
      success: function(response) {
        // Handle successful response
        console.log(response); // You can do something with the response from the server
      },
      error: function(xhr, textStatus, errorThrown) {
        // Handle error
        console.log(textStatus, errorThrown);
      }
    });
  });
});
