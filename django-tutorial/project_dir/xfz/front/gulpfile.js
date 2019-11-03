
var gulp = require("gulp");
var cssnano = require("gulp-cssnano");
var rename = require("gulp-rename");
var uglify = require("gulp-uglify");
var concat = require("gulp-concat")
var cache = require("gulp-cache")
var imagemin = require("gulp-imagemin")
var scss = require('gulp-sass')
var bs = require("browser-sync").create()


var path = {
    'html': './templates/**/',
    // 'css': './src/css/',
    'scss': './src/css/',
    'js': './src/js/',
    'images': './src/images/',
    // 'css_dist': './dist/css/',
    'scss_dist': './dist/css/',
    'js_dist': './dist/js/',
    'images_dist': './dist/images/',

}

// 处理html文件的任务
gulp.task('html', function () {
    gulp.src(path.html + '*.html')
        .pipe(bs.stream())

})

// 定义一个css任务
// gulp.task("css", function () {
//     gulp.src(path.css + "*.css")
//         .pipe(cssnano())
//         .pipe(rename({"suffix": ".min"}))
//         .pipe(gulp.dest(path.css_dist))
//         .pipe(bs.stream())
//
// })

// 定义一个scss任务
gulp.task("scss", function () {
    gulp.src(path.scss + "*.scss")
        .pipe(scss())
        .pipe(rename({"suffix": ".min"}))
        .pipe(gulp.dest(path.scss_dist))
        .pipe(bs.stream())

})

// 处理js文件的任务
gulp.task("js", function () {
    gulp.src(path.js + "*.js")
        .pipe(uglify())
        .pipe(rename({'suffix': '.min'}))
        .pipe(gulp.dest(path.js_dist))
        .pipe(bs.stream())

})

// 定义处理图片文件任务
gulp.task("images", function () {
    gulp.src(path.images + "*.*")
        .pipe(cache(imagemin()))
        .pipe(gulp.dest(path.images_dist))
        .pipe(bs.stream())

})

// 定义监听文件修改的任务
gulp.task("watch", function () {
    gulp.watch(path.html + "*.html", ['html']);
    // gulp.watch(path.css + "*.css", ['css']);
    gulp.watch(path.scss + "*.scss", ['scss']);
    gulp.watch(path.js + "*.js", ['js']);
    gulp.watch(path.images + "*.*", ['images']);

})

// 初始化 browser-sync的任务
gulp.task('bs', function () {
    bs.init({
        'server': {
            'baseDir': './'
        }
    })


})

// 创建一个默认的任务
gulp.task('default', ['bs', 'watch'])
