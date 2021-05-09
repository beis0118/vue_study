<template>
  <div>
    <!--    面包屑区域-->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item
        :to="{ path: '/welcome' }"
        @click="saveNavState('/welcome')"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!--    卡片视图区域-->
    <el-card>
      <!--      搜索与添加区域-->
      <!--      分割栏,使用gutter设置每个col之间间距, 每个col使用span属性定义宽度, 总共是24-->
      <el-row :gutter="20">
        <el-col :span="7">
          <el-input placeholder="请输入内容">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="addDialogVisible = true">添加用户</el-button>
        </el-col>
      </el-row>
      <!-- 信息表格 -->
      <el-table
        :data="currTableData"
        style="width: 100%"
        :highlight-current-row="true"
        height="300"
        border
        stripe
      >
        <!-- 定义索引,index内是自定义索引内容 -->
        <el-table-column
          prop="name"
          label="ID"
          width="40"
          type="index"
          index="123"
        >
        </el-table-column>
        <el-table-column prop="date" label="日期" width="180">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="180">
        </el-table-column>
        <!-- 设置排序,需要先将sortable设置为true,根据address值进行排序,会显示在地址选项中 -->
        <el-table-column
          prop="address"
          label="地址"
          :sortable="true"
          sort-by="address"
        >
        </el-table-column>
      </el-table>
      <!-- 设置分页栏, @表示v-on,用于监听方法 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="1"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="this.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.length - 1"
      >
      </el-pagination>
      <!-- 添加用户---对话框 -->
      <el-dialog
        title="提示"
        :visible.sync="addDialogVisible"
        width="30%"
        :before-close="handleClose"
      >
        <!-- 标题 -->
        <span slot="title">添加用户</span>
        <!-- 内容主体区 -->
        <span>这是一段信息</span>
        <!-- 按钮区 -->
        <span slot="footer" class="dialog-footer">
          <el-button @click="addDialogVisible = true">取 消</el-button>
          <el-button type="primary" @click="addUser"
            >添 加</el-button
          >
        </span>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "Users",
  data() {
    return {
      tableData: [
        // 此数据用来调整顺序, 使索引值从1开始
        {
          date: "null",
          name: "null",
          address: "null"
        },
        {
          date: "2016-05-02",
          name: "Nio",
          address: "上海市普陀区金沙江路 1518 弄"
        },
        {
          date: "2016-05-04",
          name: "ChuXinY",
          address: "上海市普陀区金沙江路 1517 弄"
        },
        {
          date: "2016-05-01",
          name: "Beis",
          address: "上海市普陀区金沙江路 1519 弄"
        },
        {
          date: "2016-05-03",
          name: "褚心悦",
          address: "上海市普陀区金沙江路 1516 弄"
        }
      ],
      // 设置当前显示的data
      currTableData: [],
      pageStart: 1,
      pageEnd: 1,
      pagesize: 1,
      // 设置是否显示添加用户的对话框
      addDialogVisible: false
    };
  },
  created() {
    // 设置当前end
    this.pageEnd = this.pageStart + this.pagesize;
    // 设置当前分页
    this.currTableData = this.tableData.slice(this.pageStart, this.pageEnd);
  },
  methods: {
    addUser() {
      var info = {
        date: "2020-05-010",
        name: "Cat",
        address: "广东省深圳市南山区滨海大厦WXG"
      };
      this.tableData.push(info);
      // 更新显示值
      this.currTableData = this.tableData.slice(this.pageStart, this.pageEnd);
      this.addDialogVisible = false;
    },
    // 监听页码大小
    handleSizeChange(val) {
      console.log(val);
      // 赋值给pageEnd
      this.pageEnd = this.pageStart + val;
      console.log(this.pageEnd);
      // 截取数组
      this.currTableData = this.tableData.slice(this.pageStart, this.pageEnd);
    },
    // 改变页数, 也要进行数据展示更新
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      // 更新起始值
      this.pageStart = val * this.pagesize;
      // 更新结束值
      this.pageEnd = this.pageEnd + this.pagesize;
      this.currTableData = this.tableData.slice(this.pageStart, this.pageEnd);
    }
  }
};
</script>
<style scoped></style>
