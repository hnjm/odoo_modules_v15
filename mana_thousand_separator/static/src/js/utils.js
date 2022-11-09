/** @odoo-module **/

odoo.define("mana_thousand_separator.utils", function (require) {
  "use strict";

  var core = require("web.core");

  var formatNumber = function (value) {
    var thousandsSep = core._t.database.parameters.thousands_sep || ",";
    var decimalSep = core._t.database.parameters.decimal_point || ".";
    var str = String(value).trim();
    var sign = str.startsWith("-") ? "-" : "";
    // Remove all characters except number and decimal separator
    str = str.replace(new RegExp("[^" + decimalSep + "\\d]", "g"), "");
    // If the string starts with decimal separators, remove them
    str = str.replace(new RegExp("^\\" + decimalSep + "*"), "");
    // Insert thousand separators
    str = str.replace(/\B(?=((\d{3})+(?!\d)))/g, thousandsSep);
    // Remove invalid characters after the first decimal separator
    var splits = str.split(decimalSep);
    if (splits.length > 1) {
      str =
        splits[0] +
        decimalSep +
        splits[1].replace(new RegExp("\\" + thousandsSep, "g"), "");
    }
    // Restore sign
    str = sign + str;
    return str;
  };

  var formatFormula = function (formula) {
    if (!formula.startsWith("=")) {
      return formatNumber(formula);
    }
    var str = "";
    for (let v of formula.split(new RegExp(/([-+*/()^=\s])/g))) {
      if (!["+", "-", "*", "/", "(", ")", "^", "="].includes(v) && v.trim()) {
        v = formatNumber(v);
      }
      str += v;
    }
    return str;
  };

  var parseNumber = function (value) {
    var thousandsSep = core._t.database.parameters.thousands_sep || ",";
    var decimalSep = core._t.database.parameters.decimal_point || ".";
    var str = value;
    // Remove all thousands separators
    str = str.replace(new RegExp("\\" + thousandsSep, "g"), "");
    // Remove language-dependent decimal separator with the standard separator (.)
    str = str.replace(decimalSep, ".");
    return Number(str);
  };

  return {
    formatNumber: formatNumber,
    formatFormula: formatFormula,
    parseNumber: parseNumber,
  };
});
