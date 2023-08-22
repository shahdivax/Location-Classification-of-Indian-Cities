function previewFile() {
  const preview = document.querySelector('#preview');
  const file = document.querySelector('input[type=file]').files[0];
  const reader = new FileReader();

  reader.addEventListener("load", function () {
    preview.src = reader.result;
  }, false);

  if (file) {
    reader.readAsDataURL(file);
  }
}

const input = document.querySelector('input[type=file]');
input.addEventListener("change", previewFile);

