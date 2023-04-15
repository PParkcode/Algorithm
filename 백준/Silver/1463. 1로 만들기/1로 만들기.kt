import java.lang.Integer.min
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.LinkedHashMap



fun main(){
    val num = readLine()!!.toInt()
    val arr =Array<Int>(1000001) {0}

    for( i in 2 .. num){
        arr[i]=arr[i-1]+1

        if(i%2==0){
            arr[i]=min(arr[i],arr[i/2]+1)
        }
        if(i%3==0){
            arr[i]=min(arr[i],arr[i/3]+1)
        }
    }

    println(arr[num])
}