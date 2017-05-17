
var gulp = require('gulp');
var localScreenshots = require('gulp-local-screenshots');

gulp.task('screens', function () {
  gulp.src('./public/*.html')
  .pipe(localScreenshots({
    width: ['320'],
    type: 'png',
    zoom: 2
   }))
  .pipe(gulp.dest('./public/'));
});

