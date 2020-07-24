$(document).ready(function () {
    // import {Spinner} from 'spin.js';

    let inputs = $('div.field');

    inputs.each(function (i) {
        let field = this;
        $(this).find('input').first().change(function (e) {
            let preview = $(field).find('img').first();
            loadImage(
                e.target.files[0],
                function (img) {
                    preview.attr('src', img.toDataURL());
                    preview.css('display', 'initial')
                },
                {orientation: true, canvas: false}
            );
        })
    })

    // $(".picture-input").change(function (e) {
    //     let preview = $('#avatar-preview');
    //     // preview.attr('src','')
    //     // let spinner = new Spinner().spin(preview);
    //     loadImage(
    //         e.target.files[0],
    //         function (img) {
    //             preview.attr('src', img.toDataURL())
    //         },
    //         {orientation: true, canvas: false} // Options
    //     );
    //     // spinner.stop();
    // })
})