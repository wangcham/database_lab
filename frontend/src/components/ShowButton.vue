<template>
    <div class="all">
        <div class="buttons">
            <el-button type="primary" @click="borrow=true">借书</el-button>
            <el-button type="primary" @click="returnbook=true">还书</el-button>
            <el-button type="round" @click="addu=true">新增用户</el-button>
            <el-button type="round" @click="deleteu=true">删除用户</el-button>
            <el-button type="info" @click="showuserlist=true,showborrowlist=false">展示用户列表</el-button>
            <el-button type="info" @click="showuserlist=false,showborrowlist=true">展示借阅信息</el-button>
        </div>
        <div class="content">
            <ShowUserList v-if="showuserlist"></ShowUserList>
            <ShowBorrowList v-if="showborrowlist"></ShowBorrowList>
        </div>

        <el-dialog v-model="addu" title="新增用户">
            <AddUser></AddUser>
        </el-dialog>

        <el-dialog v-model="deleteu" title="删除用户">
            <DeleteUser></DeleteUser>
        </el-dialog>

        <el-dialog v-model="borrow" title="借书">
            <BorrowBook></BorrowBook>
        </el-dialog>

        <el-dialog v-model="returnbook" title="还书">
            <ReturnBook></ReturnBook>    
        </el-dialog>
    </div>
</template>
<script>
import ShowUserList from './MainPage/ShowUserList.vue';
import ShowBorrowList from './MainPage/ShowBorrowList.vue';
import AddUser from './MainPage/AddUser.vue';
import DeleteUser from './MainPage/DeleteUser.vue';
import BorrowBook from './MainPage/BorrowBook.vue';
import ReturnBook from './MainPage/ReturnBook.vue';

export default{
    name:'ShowButton',
    components:{
        ShowUserList,
        ShowBorrowList,
        AddUser,
        DeleteUser,
        BorrowBook,
        ReturnBook,
    },
    data(){
        return{
            showuserlist:true,
            showborrowlist:false,
            
            borrow:false,
            returnbook:false,
            addu:false,
            deleteu:false,
        }
    },
}

</script>

<style>
.all{
    display: flex;
    flex-direction: column;
}
.content{
    margin-top:50px;
}
.buttons{
    display:flex;
    position:fixed;
    top:10px;
    justify-content: space-between;
    align-items: center;
}
</style>