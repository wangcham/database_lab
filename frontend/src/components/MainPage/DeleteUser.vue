<template>
    <div>
        <el-input placeholder="请输入要删除的学生的学号" v-model="id"/>
        <el-button @click="submit" style="margin-top:10px">提交</el-button>
    </div>
</template>

<script>
import axios from 'axios'
import {ElMessage} from 'element-plus'
import common from '../../assets/common/common'
export default{
    name:'DeleteUser',
    data(){
        return{
            id:'',
        }
    },
    methods:{
        submit(){
            axios.post(common.backend_prefix+'/deleteuser',{
                id:this.id,
            }).then(
                response =>{
                        if(response.data.status=='fail'){
                            ElMessage.error(response.data.message)
                        }else{
                            ElMessage.success(response.data.message)
                        }
                    }
            ).catch(
                error =>{
                    console.log(error)
                }
            )
        },
    }
}
</script>

