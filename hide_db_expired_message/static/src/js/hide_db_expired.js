odoo.define('hide_db_expired_message.hide_db_expired', function (require) {
    "use strict";

    var core = require('web.core');

    core.bus.on('web_client_ready', null, function () {
        console.log("Custom JavaScript loaded.");
        setTimeout(function () {
            // Hide the o_blockUI element
            var blockUIElement = document.querySelector('.o_blockUI');
            if (blockUIElement) {
                blockUIElement.style.setProperty('display', 'none', 'important');
            }
            // Hide the next element after o_blockUI
            var nextBlockUIElement = blockUIElement ? blockUIElement.nextElementSibling : null;
            if (nextBlockUIElement) {
                nextBlockUIElement.style.setProperty('display', 'none', 'important');
            }
        }, 1); // Delay of 1 second (1000 milliseconds)
    });
});
