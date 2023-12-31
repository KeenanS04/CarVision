document.addEventListener('DOMContentLoaded', function () {
    var image = document.getElementById('image');
    var input = document.getElementById('imageInput');
    var form = document.getElementById('uploadForm');
    var cropper;

    input.addEventListener('change', function (e) {
        var files = e.target.files;
        if (files && files.length > 0) {
            image.style.display = 'block';
            var reader = new FileReader();
            reader.onload = function (e) {
                image.src = e.target.result;
                if (cropper) {
                    cropper.destroy();
                }
                cropper = new Cropper(image, {
                    aspectRatio: 16 / 9,
                    crop(event) {
                        document.getElementById('cropX').value = event.detail.x;
                        document.getElementById('cropY').value = event.detail.y;
                        document.getElementById('cropWidth').value = event.detail.width;
                        document.getElementById('cropHeight').value = event.detail.height;
                    },
                });
            };
            reader.readAsDataURL(files[0]);
        }
    });

    // You can also add event listener to form submission if needed
});
