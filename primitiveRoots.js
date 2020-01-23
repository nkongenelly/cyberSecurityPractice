

//Finding Primitive numbers of prime numbers
//Define variables
var n =13;
var a,d,modes;
var storage = [];
var one = [];

     var results = [];

//display the relative prime numbers of n
for(var k = 1; k < n; k++){
storage.push(k);
}
    document.write("a = " + storage);
document.write("<br>");

//on each 'a' , calculate, a to power m mode n
for(var i=1; i<n; i++){
	for(var m =1; m<n; m++){

    a = Math.pow(i,m);
        d = a%n;
        storage.push(d);
       
     }
   
}

 document.write("<br>");
 //DIVIDE THE VALUES TO GET ONLY VALUES FOR EACH ROW
modes =storage.splice(0,n-1);
document.write("<br>");
document.write("VERTICAL = " + modes);
document.write("<br>");
document.write("CELL VALUES = " + storage);
//split to the vertical cells to create a table,  VALUES TO BE IN THEIR OWN ROWS
 document.write("<br>");
var i,j,temparray=[],chunk = n-1;
for (i=0,j=storage.length; i<j; i+=chunk) {
	var b =storage.slice(i,i+chunk);
    temparray.push(b);

}

document.write("MODE N. N IS "+ temparray[1]);
    //Determine which are the prime factors of n


    for(i =0; i<n-1; i++){  
    var arr = temparray[i];
var sorted_arr = arr.slice().sort();

        var  nonRepititive =[];
   for(var g=1; g<temparray[i].length; g++){
      if(sorted_arr[g - 1] != sorted_arr[g]){

      nonRepititive.push(1);

           if( nonRepititive.length == n-2){
             results.push(modes[i]);
           } 
       }
 
   }
     document.write("<br>");
     console.log(Results);
document.write("Results are: " + results);

    }
    //document.write("Results are: " + results);
