<template>
  <div>
    <a @keyup.esc="exit_screen"></a>
    <video ref="videoPlayer" class="video-js vjs-big-play-centered vjs-default-skin">" @keyup.esc="exit_screen"
    style="margin:auto; top:0;bottom:0;left:0;right:0;"></video>
    <el-row>
      <el-button @click="change">开始/暂停</el-button>
      <el-button @click="set_time" type="primary">跳转</el-button>
      <el-button @click="fast" type="success">倍速播放</el-button>
      <el-button @click="full_screen" type="info">全屏</el-button>
      <el-button @click="change_video" type="warning">切换视频</el-button>
      <el-input v-model="volume" placeholder="请输入音量" style="width: 10%">切换音量></el-input>
      <el-button @click="change_volume" type="warning">切换音量</el-button>
    </el-row>
  </div>
</template>

<script>
import videojs from 'video.js'

export default {
  name: 'VideoPlayer',
  // 父组件通过props向下传递数据给子组件，子组件通过events给父组件发送消息。
  props: {
    options: {
      type: Object,
      default () {
        return {}
      }
    }
  },
  methods: {
    change () { // 切换播放状态
      if (this.player.paused()) return this.player.play()
      return this.player.pause()
    },
    set_time () { // 设置当前播放时间
      console.log(this.player.currentTime(123))
    },
    fast () { // 倍速
      this.player.playbackRate(2)
    },
    full_screen () { // 设置网页全屏
      this.player.enterFullWindow()
    },
    exit_screen () { // 设置退出全屏
      this.player.exitFullWindow()
    },
    change_video () { // 切换视频
      this.player.src(require('../assets/video/langzihuitou.mp4'))
    },
    change_volume () { // 切换音量, 0-1
      console.log(this.$data.volume)
      this.player.volume(this.$data.volume)
    }
  },
  data () {
    return {
      player: null,
      volume: null
    }
  },
  mounted () {
    // 所有器件挂载完以后, 执行此函数
    this.player = videojs(this.$refs.videoPlayer, this.options, function onPlayerReady () {
      console.log('onPlayerReady', this)
      // 事件events    绑定事件用on    移除事件用off
    })
  },
  beforeDestroy () {
    if (this.player) {
      this.player.dispose()
    }
  }
}
</script>
<style>

</style>
