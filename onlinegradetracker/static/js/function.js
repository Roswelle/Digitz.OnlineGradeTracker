
      function openForm() {
        document.getElementById("popupForm").style.display = "block";
      }
      function closeForm() {
        document.getElementById("popupForm").style.display = "none";
      }
      function openModal() {
        document.getElementById("modal").style.display = "block";
    }

    function closeModal() {
        document.getElementById("modal").style.display = "none";
    }

    var table = document.getElementById('gradingtable');
    var rows = table.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++){
      rows[i].onclick = function() {
        openModal();
      }
    }