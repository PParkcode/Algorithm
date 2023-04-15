fun main(){
    val count = readLine()!!.toInt()
    var answer=0
    repeat(count){
        var (width,height,num) = readLine()!!.split(" ").map { it.toInt() }
        var arr= Array(height){IntArray(width) }
        repeat(num){
            var (a,b) = readLine()!!.split(" ").map { it.toInt() }
            arr[b][a]=1
        }

        for(i in 0 until height){
            for(j in 0 until width){
                if(arr[i][j]==1){
                    arr=dfs(j,i,arr,width,height)
                    answer++
                }
            }
        }
        println(answer)
        answer=0
    }

}
fun dfs(x:Int,y:Int,arr:Array<IntArray>,w:Int,h:Int):Array<IntArray>{
    arr[y][x]=0
    var rarray=arr
    if(y-1>=0){
        if(arr[y-1][x]==1){
            rarray=dfs(x,y-1,arr,w,h)
        }
    }
    if(y+1<h){
        if(arr[y+1][x]==1){
            rarray=dfs(x,y+1,arr,w,h)
        }
    }
    if(x-1>=0){
        if(arr[y][x-1]==1){
            rarray=dfs(x-1,y,arr,w,h)
        }
    }
    if(x+1<w){
        if(arr[y][x+1]==1){
            rarray=dfs(x+1,y,arr,w,h)
        }
    }
    return rarray


}