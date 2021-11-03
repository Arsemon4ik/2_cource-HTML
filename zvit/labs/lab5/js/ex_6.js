$('#crop').cropbox({
        width: 200,
        height: 200
    },
    function() {
            //on load
            console.log('Url: ' + this.getDataURL());
    }).on('cropbox', function(e, data) {
    console.log('crop window: ' + data);
    });


