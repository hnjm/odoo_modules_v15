/** @odoo-module **/

odoo.define("mana_thousand_separator.number_input", function (require) {
  "use strict";
  var utils = require("mana_thousand_separator.utils");
  $(document).on("input", "input[data-twts]", function (e) {
    e.preventDefault();
    this.value = utils.formatNumber(this.value);
    var target = document.getElementById(this.dataset.twts);
    if (target) {
      target.value = utils.parseNumber(this.value);
    }
  });
});
