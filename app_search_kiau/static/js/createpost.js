// for select input
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems, {

  });
});

// for book_description
$('#textarea1').val('New Text');
 M.textareaAutoResize($('#textarea1'));

// input characterCounter
 $(document).ready(function() {
  $('input#book_name , input#book_author , input#book_year , input#book_rank , textarea#textarea1').characterCounter();
});
