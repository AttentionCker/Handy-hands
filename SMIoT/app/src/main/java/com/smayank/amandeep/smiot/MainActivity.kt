package com.smayank.amandeep.smiot

import android.animation.ValueAnimator
import android.annotation.SuppressLint
import android.app.AlertDialog
import android.content.Context
import android.content.DialogInterface
import android.content.Intent
import android.net.Uri
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import kotlinx.android.synthetic.main.activity_main.*
import android.text.method.ScrollingMovementMethod
import android.widget.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        textView4.setOnClickListener{

            val webIntent = Intent(Intent.ACTION_VIEW, Uri.parse("http://smayank.com"))
            startActivity(webIntent)

        }



        imageView.setOnClickListener {



            val dialog = AlertDialog.Builder(this, R.style.DialogTheme)
            val dialogView = layoutInflater.inflate(R.layout.log,null)

            val logdisplay=dialogView.findViewById<TextView>(R.id.textView)

            logdisplay.setScroller(Scroller(this))
            logdisplay.isVerticalScrollBarEnabled = true
            logdisplay.movementMethod = ScrollingMovementMethod()

            dialog.setView(dialogView)
            dialog.setCancelable(false)
            val queue = Volley.newRequestQueue(this)

            val stringRequest = StringRequest(Request.Method.GET, "http://smayank.com/smiot/appinfo",
                    Response.Listener<String> { response ->
                        val te = response.toString()
                        logdisplay.text=te
                    },
                    Response.ErrorListener {error ->  makeToast("Error: $error")})

            queue.add(stringRequest)

            dialog.setPositiveButton("OK") { dialogInterface: DialogInterface, i: Int ->
            }

            dialog.show()





        }


    }


    @SuppressLint("WrongConstant")
    override fun onResume() {
        super.onResume()

        textView4.text="Smayank.com"
        textView4.isEnabled=true



        sendMode()

        button9.setOnClickListener {

            editMode()

        }

        button12.setOnClickListener {

            val preferencelog= this.getSharedPreferences("logurl",Context.MODE_PRIVATE)
            val url=preferencelog.getString("ur","")

            val dialog = AlertDialog.Builder(this, R.style.DialogTheme)
            val dialogView = layoutInflater.inflate(R.layout.log,null)

            val logdisplay=dialogView.findViewById<TextView>(R.id.textView)

            logdisplay.setScroller(Scroller(this))
            logdisplay.isVerticalScrollBarEnabled = true
            logdisplay.movementMethod = ScrollingMovementMethod()

            dialog.setView(dialogView)
            dialog.setCancelable(false)
            val queue = Volley.newRequestQueue(this)

            val stringRequest = StringRequest(Request.Method.GET, url,
                    Response.Listener<String> { response ->
                        val te = response.toString()
                        logdisplay.text=te
                    },
                    Response.ErrorListener {error ->  makeToast("Error: $error")})

            queue.add(stringRequest)

            dialog.setPositiveButton("OK") { dialogInterface: DialogInterface, i: Int ->

            }

            dialog.setNeutralButton("EDIT"){ dialogInterface: DialogInterface, i: Int ->


                val dialog = AlertDialog.Builder(this, R.style.DialogTheme)
                val dialogView = layoutInflater.inflate(R.layout.editlog,null)
                dialog.setView(dialogView)
                dialog.setCancelable(false)

                val led=dialogView.findViewById<EditText>(R.id.editText3)

                dialog.setPositiveButton("SAVE") { dialogInterface: DialogInterface, i: Int ->

                    if (led.text.isNotEmpty()){

                        val preference= this.getSharedPreferences("logurl",Context.MODE_PRIVATE)
                        val eTime=preference.edit()
                        eTime.putString("ur",led.text.toString())
                        eTime.apply()

                        onResume()

                    }


                }

                dialog.setNegativeButton("CANCEL"){ dialogInterface: DialogInterface, i: Int ->
                }

                dialog.show()

            }
            dialog.show()
        }

    }

    fun requestButton(requ:String, codu:String){
        sendPost(requ+codu)
    }

    fun editButton(buttt:Button,butt:String, requ:String, codu:String, namu:String){

        val dialog = AlertDialog.Builder(this,R.style.DialogTheme)
        val dialogView = layoutInflater.inflate(R.layout.editpost,null)

        dialog.setView(dialogView)
        dialog.setCancelable(false)

        val n=dialogView.findViewById<EditText>(R.id.editText)
        val cod=dialogView.findViewById<EditText>(R.id.editText2)

        n.setText(namu, TextView.BufferType.EDITABLE)
        dialogView.findViewById<EditText>(R.id.editText3).setText(requ, TextView.BufferType.EDITABLE)
        cod.setText(codu, TextView.BufferType.EDITABLE)

        dialog.setPositiveButton("SAVE") { dialogInterface: DialogInterface, i: Int ->
            val name=n.text.toString()
            val req=cod.text.toString()

            if (req.isNotEmpty()){

                val preference= this.getSharedPreferences(butt,Context.MODE_PRIVATE)
                val eTime=preference.edit()
                eTime.putString("name",name)
                eTime.putString("req",dialogView.findViewById<EditText>(R.id.editText3).text.toString())
                eTime.putString("code",req)
                eTime.apply()

                editMode()


            }


        }
        dialog.setNegativeButton("CANCEL"){ dialogInterface: DialogInterface, i: Int ->
        }

        dialog.show()

    }



    fun sendMode(){


        button9.text="EDIT"
        textView3.text="SMIoT"

        val buttonid=button.id.toString()
        val buttonid2=button2.id.toString()
        val buttonid3=button3.id.toString()
        val buttonid4=button4.id.toString()
        val buttonid5=button5.id.toString()
        val buttonid6=button6.id.toString()
        val buttonid7=button7.id.toString()
        val buttonid8=button8.id.toString()
        val buttonid10=button10.id.toString()
        val buttonid11=button11.id.toString()

        val preference= this.getSharedPreferences(buttonid,Context.MODE_PRIVATE)
        val n=preference.getString("name","BUTTON")
        val r=preference.getString("req","http://smayank.com/iot?id=")
        val c=preference.getString("code","0000")
        button.text=n


        val preference2= this.getSharedPreferences(buttonid2,Context.MODE_PRIVATE)
        val n2=preference2.getString("name","BUTTON")
        val r2=preference2.getString("req","http://smayank.com/iot?id=")
        val c2=preference2.getString("code","0000")
        button2.text=n2

        val preference3= this.getSharedPreferences(buttonid3,Context.MODE_PRIVATE)
        val n3=preference3.getString("name","BUTTON")
        val r3=preference3.getString("req","http://smayank.com/iot?id=")
        val c3=preference3.getString("code","0000")
        button3.text=n3

        val preference4= this.getSharedPreferences(buttonid4,Context.MODE_PRIVATE)
        val n4=preference4.getString("name","BUTTON")
        val r4=preference4.getString("req","http://smayank.com/iot?id=")
        val c4=preference4.getString("code","0000")
        button4.text=n4

        val preference5= this.getSharedPreferences(buttonid5,Context.MODE_PRIVATE)
        val n5=preference5.getString("name","BUTTON")
        val r5=preference5.getString("req","http://smayank.com/iot?id=")
        val c5=preference5.getString("code","0000")
        button5.text=n5

        val preference6= this.getSharedPreferences(buttonid6,Context.MODE_PRIVATE)
        val n6=preference6.getString("name","BUTTON")
        val r6=preference6.getString("req","http://smayank.com/iot?id=")
        val c6=preference6.getString("code","0000")
        button6.text=n6

        val preference7= this.getSharedPreferences(buttonid7,Context.MODE_PRIVATE)
        val n7=preference7.getString("name","BUTTON")
        val r7=preference7.getString("req","http://smayank.com/iot?id=")
        val c7=preference7.getString("code","0000")
        button7.text=n7

        val preference8= this.getSharedPreferences(buttonid8,Context.MODE_PRIVATE)
        val n8=preference8.getString("name","BUTTON")
        val r8=preference8.getString("req","http://smayank.com/iot?id=")
        val c8=preference8.getString("code","0000")
        button8.text=n8

        val preference10= this.getSharedPreferences(buttonid10,Context.MODE_PRIVATE)
        val n10=preference10.getString("name","BUTTON")
        val r10=preference10.getString("req","http://smayank.com/iot?id=")
        val c10=preference10.getString("code","0000")
        button10.text=n10

        val preference11= this.getSharedPreferences(buttonid11,Context.MODE_PRIVATE)
        val n11=preference11.getString("name","BUTTON")
        val r11=preference11.getString("req","http://smayank.com/iot?id=")
        val c11=preference11.getString("code","0000")
        button11.text=n11

        button.setOnClickListener {requestButton(r!!,c!!)}
        button2.setOnClickListener {requestButton(r2!!,c2!!)}
        button3.setOnClickListener {requestButton(r3!!,c3!!)}
        button4.setOnClickListener {requestButton(r4!!,c4!!)}
        button5.setOnClickListener {requestButton(r5!!,c5!!)}
        button6.setOnClickListener {requestButton(r6!!,c6!!)}
        button7.setOnClickListener {requestButton(r7!!,c7!!)}
        button8.setOnClickListener {requestButton(r8!!,c8!!)}
        button10.setOnClickListener {requestButton(r10!!,c10!!)}
        button11.setOnClickListener {requestButton(r11!!,c11!!)}


    }

    fun editMode(){

        textView4.text=""
        textView4.isEnabled=false


        val buttonid=button.id.toString()
        val buttonid2=button2.id.toString()
        val buttonid3=button3.id.toString()
        val buttonid4=button4.id.toString()
        val buttonid5=button5.id.toString()
        val buttonid6=button6.id.toString()
        val buttonid7=button7.id.toString()
        val buttonid8=button8.id.toString()
        val buttonid10=button10.id.toString()
        val buttonid11=button11.id.toString()


        val preference= this.getSharedPreferences(buttonid,Context.MODE_PRIVATE)
        val n=preference.getString("name","BUTTON")
        val r=preference.getString("req","http://smayank.com/iot?id=")
        val c=preference.getString("code","0000")
        button.text=n


        val preference2= this.getSharedPreferences(buttonid2,Context.MODE_PRIVATE)
        val n2=preference2.getString("name","BUTTON")
        val r2=preference2.getString("req","http://smayank.com/iot?id=")
        val c2=preference2.getString("code","0000")
        button2.text=n2

        val preference3= this.getSharedPreferences(buttonid3,Context.MODE_PRIVATE)
        val n3=preference3.getString("name","BUTTON")
        val r3=preference3.getString("req","http://smayank.com/iot?id=")
        val c3=preference3.getString("code","0000")
        button3.text=n3

        val preference4= this.getSharedPreferences(buttonid4,Context.MODE_PRIVATE)
        val n4=preference4.getString("name","BUTTON")
        val r4=preference4.getString("req","http://smayank.com/iot?id=")
        val c4=preference4.getString("code","0000")
        button4.text=n4

        val preference5= this.getSharedPreferences(buttonid5,Context.MODE_PRIVATE)
        val n5=preference5.getString("name","BUTTON")
        val r5=preference5.getString("req","http://smayank.com/iot?id=")
        val c5=preference5.getString("code","0000")
        button5.text=n5

        val preference6= this.getSharedPreferences(buttonid6,Context.MODE_PRIVATE)
        val n6=preference6.getString("name","BUTTON")
        val r6=preference6.getString("req","http://smayank.com/iot?id=")
        val c6=preference6.getString("code","0000")
        button6.text=n6

        val preference7= this.getSharedPreferences(buttonid7,Context.MODE_PRIVATE)
        val n7=preference7.getString("name","BUTTON")
        val r7=preference7.getString("req","http://smayank.com/iot?id=")
        val c7=preference7.getString("code","0000")
        button7.text=n7

        val preference8= this.getSharedPreferences(buttonid8,Context.MODE_PRIVATE)
        val n8=preference8.getString("name","BUTTON")
        val r8=preference8.getString("req","http://smayank.com/iot?id=")
        val c8=preference8.getString("code","0000")
        button8.text=n8

        val preference10= this.getSharedPreferences(buttonid10,Context.MODE_PRIVATE)
        val n10=preference10.getString("name","BUTTON")
        val r10=preference10.getString("req","http://smayank.com/iot?id=")
        val c10=preference10.getString("code","0000")
        button10.text=n10

        val preference11= this.getSharedPreferences(buttonid11,Context.MODE_PRIVATE)
        val n11=preference11.getString("name","BUTTON")
        val r11=preference11.getString("req","http://smayank.com/iot?id=")
        val c11=preference11.getString("code","0000")
        button11.text=n11



        val animator: ValueAnimator = ValueAnimator.ofFloat(0f, 360f)
        animator.duration =300
        animator.start()

        animator.addUpdateListener { animation ->
            val animatedValue = animation.animatedValue as Float
            imageView.rotation = animatedValue
        }



        textView3.text="SMIoT : Edit Mode"

        button.setOnClickListener {editButton(button,buttonid,r!!,c!!,n!!)}
        button2.setOnClickListener {editButton(button2,buttonid2,r2!!,c2!!,n2!!)}
        button3.setOnClickListener {editButton(button3,buttonid3,r3!!,c3!!,n3!!)}
        button4.setOnClickListener {editButton(button4,buttonid4,r4!!,c4!!,n4!!)}
        button5.setOnClickListener {editButton(button5,buttonid5,r5!!,c5!!,n5!!)}
        button6.setOnClickListener {editButton(button6,buttonid6,r6!!,c6!!,n6!!)}
        button7.setOnClickListener {editButton(button7,buttonid7,r7!!,c7!!,n7!!)}
        button8.setOnClickListener {editButton(button8,buttonid8,r8!!,c8!!,n8!!)}
        button10.setOnClickListener {editButton(button10,buttonid10,r10!!,c10!!,n10!!)}
        button11.setOnClickListener {editButton(button11,buttonid11,r11!!,c11!!,n11!!)}

        button9.text="<--"

        button9.setOnClickListener {
            onResume()

            val animator: ValueAnimator = ValueAnimator.ofFloat(360f,0f)
            animator.duration =300
            animator.start()

            animator.addUpdateListener { animation ->
                val animatedValue = animation.animatedValue as Float
                imageView.rotation = animatedValue
            }


        }

    }


    fun sendPost(url:String){

        val queue = Volley.newRequestQueue(this)

        val stringRequest = StringRequest(Request.Method.GET, url,
                Response.Listener<String> { response ->
                    val te = response.toString()
                    makeToast(te)
                },
                Response.ErrorListener {error ->  makeToast("Error: $error")})

        queue.add(stringRequest)

    }

    fun makeToast(t:String){
        Toast.makeText(this,t, Toast.LENGTH_LONG).show()
    }
}
