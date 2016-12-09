$(document).ready(function(){
  button_state();
    $('#client').change(function(){
      button_state();
      input_data = {
        'ajax_data_type' : 'server',
        'key' : this.value
      }
      if (!$('#server').is(':disabled'))
        $('#run_command').prop('disabled', true);
      if (parseInt(input_data.key) > 0) {
        $.ajax({
            'url' : 'ajax_main',
            'data' : input_data,
            dataType: 'json',
            success: function (json) {
                var
                  key,
                  value,
                  listitems = '<option value="0" selected>select server</option>';
                for (key in json) {
                    value = json[key]
                    listitems += '<option value="' + key +
                    '" class="os-' + json[key].os + '">' +
                    json[key].name + ' (' + json[key].ip + ')</option>'
                }
                $('#server').removeAttr('disabled').empty().append(listitems)
             }
        });
      }
      button_state();
    });
    $('#server').change(function(){
      button_state();
      var selected_server = $('#server option:selected').attr('class');
      if (selected_server !== undefined) {
        input_data = {
          'ajax_data_type' : 'command',
          'key' : selected_server.split('-')[1]
        }
        if (parseInt(input_data.key) > 0) {
          $.ajax({
              'url' : 'ajax_main',
              'data' : input_data,
              dataType: 'json',
              success: function (json) {
                  var
                    key,
                    value,
                    listitems = '<option value="0" selected>select command</option>';
                  for (key in json) {
                      value = json[key]
                      listitems += '<option value="' + key + '">' + json[key] + '</option>'
                  }
                  $('#run_command').removeAttr('disabled').empty().append(listitems);
               }
          });
        }
        button_state();
      }
    });

    $('#run_command').change(function(){
      button_state();
    });
    function button_state() {
      var
      client = $('#client option:selected'),
      server = $('#server option:selected'),
      command = $('#run_command option:selected'),
      client_val = parseInt(client.val()),
      server_val = parseInt(server.val()),
      command_val = parseInt(command.val()),
      server_text = server.text().split(' ')[0],
      command_text = command.text(),
      command_preview = '[root@' + server_text + ']# ' + command_text;
      console.log(server_text, command_text)
      console.log(command_preview)
      if (client_val !== NaN && client_val > 0 &&
        server_val !== NaN && server_val > 0 &&
        command_val !== NaN && command_val > 0) {
          $('.preview_div').show();
          $('#preview').empty().append(command_preview);
          $('#li-progress').show();
          $('#li-output').show();
          $('#li-output-label').show();
        if($('#run_button').hasClass('disable'))
          $('#run_button').removeClass('disable');
      } else {
        $('#run_button').addClass('disable');
        $('.preview_div').hide();
        $('#preview').empty();
        $('#li-progress').hide();
        $('#li-output').hide();
        $('#li-output-label').hide();        
      }
    }
    //RUN BUTTON
    //$('#run_button').click(function(){
    //  $('#command-form')[0].submit();
    //});

    //doesnt work like I expect
    $('#run_button').click(function(){ 
      $.ajax({
        'type' : 'post',
        'url' : 'ajax_main',
        //'data' : $('#command-form')[0].submit(),
        success: function() {
          alert('done')
        }
      });
    });

});
