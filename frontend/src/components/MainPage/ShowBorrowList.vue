<template>
    <div>
      <el-table :data="tableData" border>
        <el-table-column label="Borrow Date" prop="borrowdate"></el-table-column>
        <el-table-column label="Return Date" prop="returndate"></el-table-column>
        <el-table-column label="Book Name" prop="bookname"></el-table-column>
        <el-table-column label="Student ID" prop="student_id"></el-table-column>
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
        axios.post(common.backend_prefix+'/getborrowlist')
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
  
  