const gulp = require("gulp");
const concat = require('gulp-concat');
const uglify = require('gulp-uglify');
const cleanCSS = require("gulp-clean-css");
const pipeline = require('readable-stream').pipeline;
const autoprefixer = require('gulp-autoprefixer');



function cssMinify() {
  return gulp
    .src("app/static/css/*.css")
    .pipe(autoprefixer())
    .pipe(cleanCSS())
    .pipe(concat("all.css"))
    .pipe(gulp.dest("dist"))
}

function jsMinify() {
  return gulp
    .src("app/static/js/*.js")
    .pipe(uglify())
    .pipe(concat("all.js"))
    .pipe(gulp.dest("dist"))
}

exports.default = gulp.series(cssMinify, jsMinify)