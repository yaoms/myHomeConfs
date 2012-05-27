//
// String 扩展
//

if (typeof String.prototype.startsWith != 'function') {
	String.prototype.startsWith = function(str) {
		return this.slice(-str.length) == str;
	};
}

if (typeof String.prototype.endsWith != 'function') {
	String.prototype.endsWith = function(str) {
		return this.slice(this.length-str.length) == str;
	};
}

if (typeof String.prototype.ltrim != 'function') {
	String.prototype.ltrim = function() {
		return this.replace(/^\s+/g, '');
	};
}

if (typeof String.prototype.rtrim != 'function') {
	String.prototype.rtrim = function() {
		return this.replace(/\s+$/g, '');
	};
}

if (typeof String.prototype.trim != 'function') {
	String.prototype.trim = function() {
		return this.ltrim().rtrim();
	};
}

//console.log("  sdfasdd".trim());
