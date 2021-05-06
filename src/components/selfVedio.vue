<template>
  <div style="width: 100%;height: 100%">
    <VideoPlayer ref="ewq" id="player" :options="videoOptions">
    </VideoPlayer>
  </div>
</template>

<script>
import VideoPlayer from '@/components/VideoPlayer.vue'

export default {
  name: 'selfVedio',
  components: {
    VideoPlayer
  },
  data () {
    return {
      videoOptions: {
        playbackRates: [0.5, 1, 1.5, 2],
        loop: true,
        poster: require('../assets/cxy.jpg'),
        // width: '500',
        // autoplay: true,
        controls: true,
        aspectRatio: '16:9',
        preload: 'auto',
        sources: [
          {
            src: require('../assets/video/茄子蛋 - 浪流连.mp4'),
            type: 'video/mp4'
          }
        ]
      }
    }
  }
}

</script>
<style>
/*停止播放显示按钮*/
.vjs-paused .vjs-big-play-button, .vjs-paused.vjs-has-started .vjs-big-play-button {
  display: block;
}

/*播放按钮变成圆形*/
.video-js .vjs-big-play-button{
  font-size: 2.5em;
  line-height: 2.3em;
  height: 2.5em;
  width: 2.5em;
  -webkit-border-radius: 2.5em;
  -moz-border-radius: 2.5em;
  border-radius: 2.5em;
  background-color: #73859f;
  background-color: rgba(115,133,159,.5);
  border-width: 0.15em;
  margin-top: -1.25em;
  margin-left: -1.75em;
}
/* 中间的播放箭头 */
.vjs-big-play-button .vjs-icon-placeholder {
  font-size: 1.63em;
}
/* 加载圆圈 */
.vjs-loading-spinner {
  font-size: 2.5em;
  width: 2em;
  height: 2em;
  border-radius: 1em;
  margin-top: -1em;
  margin-left: -1.5em;
}
</style>
