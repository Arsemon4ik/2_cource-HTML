$( function() {
    $( ".widget input[type=submit], .widget button" ).button();
    $( "button, input" ).click( function( event ) {
      event.preventDefault();
    } );
  } );


  $( function() {
    var availableTags = [
      "BASIC",
      "C",
      "C++",
      "Java",
      "JavaScript",
      "PHP",
      "Python",
      "Ruby",
      "Scheme"
    ];
    $( "#tags" ).autocomplete({
      source: availableTags
    });
  } );



  $( function() {
    $( "#progressbar" ).progressbar({
      value: 50
    });
  } );