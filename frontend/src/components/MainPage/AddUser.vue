<template>
    <div class="input">
  <div class="input-item">
    <el-input v-model="name" placeholder="please enter name" />
  </div>
  <div class="input-item">
    <el-input v-model="id" placeholder="please enter student id" />
  </div>
  <div class="input-item">
    <el-input v-model="dept" placeholder="please enter department" />
  </div>
  <div class="submitbutton">
    <el-button @click="submit">提交</el-button>
  </div>
</div>

</template>
<script>
import common from '../../assets/common/common'
import axios from 'axios'
import {ElMessage} from 'element-plus'
    export default{
        name:'AddUser',
        data(){
            return{
                name:'',
                id:'',
                dept:'',
            }
        },
        methods:{
            submit(){
                axios.post(common.backend_prefix+'/adduser',{
                    name:this.name,
                    id:this.id,
                    dept:this.dept,
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
.input {
  display: flex;
  flex-direction: column;
}

.input-item {
  margin-bottom: 10px; /* 调整间距大小，可以根据需要进行调整 */
}


.submitbutton{
    margin-top: 20px;
}
</style>