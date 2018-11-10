$(document).ready(function () {
  $("#translate").click(function () {
    var txt = $("#phrase").val();
    $.ajax({
      url: "http://localhost:5000/feed",
      type: "POST",
      contentType: "application / json",
      dat: JSON.stringify({ "load": txt }),
      success: function (data) {
        if ("translatedtext in data") {
          $("#main-table").append("<tr id=" + data.uid + "><td" + data.text + "</td><td>" + data.translatedText + "</td><td>" + data.status + "</td></tr>")
        } else {
          $("#main-table").append("<tr id=" + data.uid + "><td>" + data.text + "</td><td> </td><td>" + data.status + "</td></tr>")
        }
      },
    });
  });

  setInterval(checkUpdates, 15000);
  function checkUpdates() {
    $("#main-table").children().each(function () {
      var state = $(this).children().last().text();
      var uid = $(this).attr("id");
      console.log(uid);
      if (state == "new" || state == "translating") {
        $.ajax({
          url: "http://localhost:5000/get-update",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify({"uuid": uid }),
          success: function (data) {
            if ("translatedText" in data) {
              $("#" + uid).remove();
              $("#main-table").append("<tr id=" + data.uid + "><td" + data.text + "</td><td>" + data.translatedText + "</td><td>" + data.status + "</td></tr>")
            } else {
              $("#" + uid).children().last().text(data.status);
            }
          }
        });
      }
    });
  }

})
