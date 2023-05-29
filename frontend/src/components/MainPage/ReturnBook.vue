<template>
    <div>
        <div class="input-item">
    <el-input v-model="id" placeholder="please enter student id" />
  </div>
  <div class="input-item">
    <el-input v-model="bookname" placeholder="please enter book name" />
  </div>
  <el-button @click="submit">确定</el-button>
    </div>
</template>

<script>
import common from '../../assets/common/common'
import axios from 'axios'
import {ElMessage} from 'element-plus'
export default{
    name:'BorrowBook',
    data(){
        return{
            bookname:'',
            id:'',
        }
    },
    methods:{
        submit(){
            axios.post(common.backend_prefix+'/returnbook',{
                    id:this.id,
                    bookname:this.bookname,
                }).then(
                    response =>{
                        if(response.data.status=='fail'){
                            ElMessage.error(response.data.message)
                        }else{
                            ElMessage.success(response.data.message)
                            location.reload()
                        }
                    }
                ).catch(
                    error =>{
                        console.log(error)
                    }
                )
        }
    }
}
</script>

<style>
.input-item{
    margin-bottom: 20px;
}
</style>
