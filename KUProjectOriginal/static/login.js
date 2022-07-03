function validateSize(input) {
  const fileSize = input.files[0].size / 1024 / 1024; // in MiB
  if (fileSize > 2) {
    alert('Failed to upload  as file size exceeds 2 MiB');
    input.value = "";
  }
}

function validateSize1(input) {
  const fileSize = input.files[0].size / 1024 / 1024; // in MiB
  if (fileSize > 0.196) {
    alert('Failed to upload  as file size exceeds 200 KiB');
    input.value = "";
  }
}
function validateSize2(input) {
  const fileSize = input.files[0].size / 1024 / 1024; // in MiB
  if (fileSize > 15) {
    alert('Failed to upload  as file size exceeds 15 MiB');
    input.value = "";
  }
}
function myFunction(prashanth) {

  var txt = document.getElementById(prashanth.id).value;
  if (txt == "true") {
    document.getElementById('sanjay').innerHTML = "<input class='info' id='choose' name='onTimef' type='file' onchange='validateSize1(this)' style='width:100%;height: 30px;font-size: 20px;'>";

  }
  else {
    document.getElementById("sanjay").innerHTML = "";
  }
}
function myFunction01(prashanth) {
  var txt = document.getElementById(prashanth.id).value;
  if (txt == "false") {
    document.getElementById('pr').innerHTML = "<th>If No,have you taken time bar permission? <br><small style='font-style: italic;'>(if Yes,Attach the order)</small></th><td><label for='nineteen'>Yes</label><input type='radio' id='nineteen' onchange='myFunction(this)' name='onTime'value='true' ><label for='nineteenF'>No</label><input id='nineteenF' onchange='myFunction(this)' type='radio' name='onTime' value='false'><span id='sanjay'></span></td>";
  }
  else {
    document.getElementById("pr").innerHTML = "";
  }
}
function myFunction02() {
  alert("This may take some time to upload your files, Depending on your Network Connection. Donot refresh or go back.");
}
function myFunction03() {
  var s = $("#check").is(':checked')
  if (s) {
    document.getElementById("span").innerHTML = "<input class='info' id='span' name='supwadd' type='text' style='text-transform: capitalize;width:100%;height: 30px;font-size: 15px;' placeholder='For Eg:University college,Kakatiya University, Warangal' required>";
  }
  else {
    document.getElementById("span").innerHTML = "<select class='info' id='span' name='supwadd' type='text' onchange='myFunction03()' style='text-transform: capitalize; width:100%;height:30px;font-size: 15px;' placeholder='Ex: University College, Kakatiya University, Warangal' required><option value='University college,Kakatiya University, Warangal.'>University college,Kakatiya University, Warangal.</option><option value='Kakatiya University College Of Engineering and Technology,Kakatiya University, Warangal'>Kakatiya University College Of Engineering and Technology,Kakatiya University, Warangal.</option><option value='University college of Pharmaucetical sciences,Kakatiya University, Warangal.'>University college of Pharmaucetical sciences,Kakatiya University, Warangal.</option><option value='University college Of Physical Education,Kakatiya University, Warangal.'>University college Of Physical Education,Kakatiya University, Warangal.</option><option value='Indian Institute of Chemical technology, Hyderabad'>Indian Institute Of Chemical Technology, Hyderabad</option>< value='Kakatiya Institute Of Technology and Science'>Kakatiya Institute Of Technology and Science"
  }
}