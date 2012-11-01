
if (!Object.create) {
    Object.create = function (o) {
        var F = function () {};
        F.prototype = o;
        return new F();
    };
}

if (!String.prototype.startsWith) {
    String.prototype.startsWith = function(str) {
        if (this.indexOf(str)) {
            return true;
        } else {
            return false;
        }
    }
}

if (!String.prototype.trim) {
    String.prototype.trim = function() {
        return this.replace(/(^\s*)(\s*$)/g, '');
    }
}

var fs = require('fs');

var Book = {
    name:"图书",
    author:"",
    prog:"etxt_maker",
    chapters:new Array(),

    loadData:function(err, data) {
        if (err) {
            throw err;
        }
        //console.log(data.toString());
        var lines = data.toString().split('\r?\n');
        var currentChapter = false;
        for (var i=0; i<lines.length; i++) {
            var line = lines[i].trim();
            if (line.startsWith('<')) {
                this.name = line.substring(1);
            } else if (line.startsWith('@')) {
                this.author = line.substring(1);
            } else if (line.startsWith('#')) {
                if (currentChapter) {
                    this.chapters.push(currentChapter);
                }
                currentChapter = Object.create(Chapter);
                currentChapter.name = line.substring(1);
            } else if (line.startsWith('!')) {
                ;
            } else if (line.length) {
                if (currentChapter) {
                    currentChapter.paragraphs.push(line);
                }
            }
        }
        if (currentChapter) {
            this.chapters.push(currentChapter);
        }
    },
    load:function(filename) {
        fs.readFile(filename, this.loadData);
    },
};


//function Book() {
//    this.name="图书";
//}
//
//Book.prototype.load = function(filename) {
//    console.log(filename);
//}

var book = Object.create(Book);
book.load("/tmp/log.txt");
console.log(book.name);
