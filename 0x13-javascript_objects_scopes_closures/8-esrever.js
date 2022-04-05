#!/usr/bin/node
// Returns reversed version of a list

exports.esrever = function (list) {
  return list.sort(function (a, b) { return b - a; });
};
