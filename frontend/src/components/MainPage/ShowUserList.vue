<template>
    <div>
      <el-table :data="tableData" border>
        <el-table-column label="Student Name" prop="name"></el-table-column>
        <el-table-column label="Student Id" prop="student_id"></el-table-column>
        <el-table-column label="Department" prop="dept"></el-table-column>
      </el-table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import common from '../../assets/common/common'
  export default {
    data() {
      return {
        tableData: []
      };
    },
    mounted() {
      this.getData();
    },
    methods: {
      getData() {
        axios.post(common.backend_prefix+'/getuserlist')
          .then(response => {
            this.tableData = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
  </script>