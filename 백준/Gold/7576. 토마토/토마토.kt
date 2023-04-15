import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main(){
    var br= BufferedReader(InputStreamReader(System.`in`))
    val (w,h) = br.readLine()!!.split(" ").map { it.toInt() }
    val graph = Array(h){IntArray(w)}
    var answer=0
    val q:Queue<Pair<Int,Int>> = LinkedList()


    for(i in 0 until h){
        graph[i]= br.readLine()!!.split(" ").map { it.toInt() }.toIntArray()
    }

    /*
    for(i in 0 until h){
        for(j in 0 until w){
            graph[i][j]=0
        }
    }
    graph[500][500]=1

     */



    for(i in 0 until h){
        for(j in 0 until w){
            if(graph[i][j]==1){
                q.add(Pair(i,j))
            }
        }
    }

    while(q.isNotEmpty()){
        answer++
        val s= q.size
       
        repeat(s){

            var(a,b) = q.remove()



            if(a-1>=0){
                if(graph[a-1][b]==0 ){
                    q.add(Pair(a-1,b))
                    graph[a-1][b]=1
                }
            }
            if(a+1<h){
                if(graph[a+1][b]==0){
                    q.add(Pair(a+1,b))
                    graph[a+1][b]=1
                }

            }
            if(b-1>=0){
                if(graph[a][b-1]==0){
                    q.add(Pair(a,b-1))
                    graph[a][b-1]=1
                }
            }
            if(b+1<w){
                if(graph[a][b+1]==0 ){
                    q.add(Pair(a,b+1))
                    graph[a][b+1]=1
                }
            }
        }

    }
    for(i in 0 until h){
        for(j in 0 until w){
            if(graph[i][j]==0){
                println(-1)
                return
            }
        }
    }
    println(answer-1)
}