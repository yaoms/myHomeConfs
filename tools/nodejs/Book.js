var fs = require('fs');

function Chapter() {
        this.name = "";
        this.paragraphs = new Array();
}

function Book() {
        this.name = "";
        this.author = "";
        this.chapters = new Array();
}

if (typeof(String.prototype.startsWith) === 'undefined') {
        String.prototype.startsWith = function (str) {
                return String(this).indexOf(str) == 0;
        };
}

if (typeof(String.prototype.trim) === 'undefined') {
        String.prototype.trim = function () {
                return String(this).replace(/^\s+|\s+$/g, '');
        };
}

Book.prototype.load = function(filename) {
        console.info("加载书籍内容: " + filename);
        var etxt = String(fs.readFileSync(filename));
        var lines = etxt.split(/\n/);
        for (var index in lines) {
                var line = lines[index];
                if (line.startsWith('书名:')) {
                        this.name = line.substring('书名:'.length).trim();
                } else if (line.startsWith('作者:')) {
                        this.author = line.substring('作者:'.length).trim();
                } else if (/ 字数:\d+/.test(line)) {
                        if (typeof(currentChapter) != 'undefined') {
                                this.chapters.push(currentChapter);
                        }
                        currentChapter = new Chapter();
                        currentChapter.name = line.replace(/ 字数:\d+/, '');
                } else if (line.startsWith('  ') && typeof(currentChapter) != 'undefined') {
                        currentChapter.paragraphs.push(line.trim());
                }
        }
        if (typeof(currentChapter) != 'undefined') {
                this.chapters.push(currentChapter);
        }
}

Book.prototype.info = function() {
        console.info("书籍信息");
        console.info(" - 书名: " + this.name);
        console.info(" - 作者: " + this.author);
        console.info("");
        console.info("=============================");
        for (var index in this.chapters) {
                var chapter  = this.chapters[index];
                console.info(" = " + chapter.name);
        }
        console.info("=============================");
}

Book.prototype.dumpTo = function(dirname) {
        console.info("导出到指定文件夹: " + dirname);
}

var book = new Book();
book.load("/home/yaoms/相公多多追着跑.etxt");
book.info();
book.dumpTo("/tmp/output");
