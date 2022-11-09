/** @odoo-module **/

odoo.define("mana_thousand_separator.basic_fields", function (require) {
  "use strict";
  var basic_fields = require("web.basic_fields");
  var utils = require("mana_thousand_separator.utils");

  basic_fields.FieldMonetary.include({
    _onInput: function () {
      this._super();
      $(this.$input).val(function (index, value) {
        return utils.formatFormula(value);
      });
    },
  });
  basic_fields.FieldFloat.include({
    _onInput: function () {
      this._super();
      if (this.formatType === "float_time") {
        return;
      }
      $(this.$input).val(function (index, value) {
        return utils.formatFormula(value);
      });
    },
  });
  basic_fields.FieldInteger.include({
    _onInput: function () {
      this._super();
      $(this.$input).val(function (index, value) {
        return utils.formatFormula(value);
      });
    },
  });
});
