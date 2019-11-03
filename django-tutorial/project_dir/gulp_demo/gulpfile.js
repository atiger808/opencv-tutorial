


var gulp = require("gulp")
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")
var bs = require("browser-sync").create()
var reload = bs.reload


// 静态服务器 监听 scss/html文件
gulp.task('serve', ['css'], function () {
    bs.init({
        server: './app/'
    });
    gulp.watch('app/css/*.css', ['css']);
    gulp.watch('app/*.html').on('change', reload);
})

gulp.task('css', function () {
    return gulp.src('./app/css/*.css')
        .pipe(cssnano())
        .pipe(rename({'suffix':'.min'}))
        .pipe(gulp.dest('app/dist/css/'))
        .pipe(reload({stream: true}))
});

gulp.task('default', ['serve'])



