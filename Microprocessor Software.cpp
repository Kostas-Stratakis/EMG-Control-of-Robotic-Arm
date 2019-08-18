//This Software was designed with Mbed platform for a Nucleo board of STM32 in C++.
// The microprocessor samples 7 seven channels of the ADC  at 2048 Hz and filters the signal from DC and 50Hz compoents.
//The the RMS of each channel is computed over window of 128 samples and a vector is sent to a PC.
// Due to analog circuit restrictions only 4 of the 7 computed values are sent via Uart mounted with Bluetooth to PC.
// The vectors sent are stored in files so that datasets are created for the traing of the pattern recogniition algorithm.
//The patern recognition done by an SVM takes place at a PC.


#include "mbed.h"

#define pi          3.14159265358979323846

InterruptIn button(USER_BUTTON);
DigitalOut led(LED1);
Serial blu (PC_4, PA_10);
Ticker timer; // declaration of interruppt 

//from which pins to sample. the last one is for the refference electrode
AnalogIn in1(PA_0);
AnalogIn in2(PA_1);
AnalogIn in3(PA_4);
AnalogIn in4(PB_0);
AnalogIn in5(PC_1);
AnalogIn in6(PC_0);
AnalogIn in7(PC_2);



//declaration of buffers for the notch filter for seven channels
float xnbuffer1[2]={0},xnbuffer2[2]={0},xnbuffer3[2]={0},xnbuffer4[2]={0},xnbuffer5[2]={0},xnbuffer6[2]={0},xnbuffer7[2]={0}; //  here the previous values of analog in  will be stored for each channel
float ynbuffer1[2]={0},ynbuffer2[2]={0},ynbuffer3[2]={0},ynbuffer4[2]={0},ynbuffer5[2]={0},ynbuffer6[2]={0},ynbuffer7[2]={0};// here the previous values of the notch filter output will be stored for each channel

//daclaration of variables to store the adc values from analog in 
float xn1=0,xn2=0,xn3=0,xn4=0,xn5=0,xn6=0,xn7=0;
//x[n-1] buffer, x[n]buffer
float xn1prev=0,xn2prev=0,xn3prev=0,xn4prev=0;
float xn1now=0,xn2now=0,xn3now=0,xn4now=0;
//declaration of the filter output variables for each channel
float yn1=0,yn2=0,yn3=0,yn4=0,yn5=0,yn6=0,yn7=0;

//declaration of window buffers after the notch. Here 128 consecutive values from them notch filter for each channel will be stored
float chan1[128]={0};
float chan2[128]={0};
float chan3[128]={0};
float chan4[128]={0};
float chan5[128]={0};
float chan6[128]={0};
float chan7[128]={0};

// declaration of feature vector to send
float x[7]={0}; 

//declaration of variable that is changed in the timer function and in button interrupt
int interval=0;
bool btn=0;

void button_press(){
    btn=!btn;
}

void timer_interrupt() {
    interval=1;
}

int main() {
blu.baud(9600); // with 9600 baud it loses samples if sending just the xn values

//declaration of main variables
int i=0; // 128 values  buffer index
int j;   //counter for rms for

// declaration of the 50Hz filter coefficients
float a1,a2,b1,r=0.99,w0=(50.0/1048.0)*pi;

//computing the coefficients
a1=2*r*cos(w0);
a2=r*r;
b1=2*cos(w0);

 // enabling the interrupts
timer.attach(&timer_interrupt, 1.0/2048.0);
button.fall(&button_press);


while (true) {
        
if(interval==1){
if(btn==1){
    
    //transfering  values from analog in objects in* to variables xn removing dc. Mbed analog in returns values in [0,1]
    //implementaion of DC filter x[n]-x[n-1]
    
    xn1now=(in1*3.6f);
    xn2now=(in2*3.6f);
    xn3now=(in3*3.6f);
    xn4now=(in4*3.6f);
    
    //xn1,2,3,4 is the output fo the DC filter
    xn1=xn1now-xn1prev;
    xn2=xn2now-xn2prev;
    xn3=xn3now-xn3prev;
    xn4=xn4now-xn4prev;
    xn5=(in5*3.6f);
    xn6=(in6*3.6f);
    xn7=(in7*3.6f);
    
    //filtering the 7 channels with the notch
    yn1=a1*ynbuffer1[1]-a2*ynbuffer1[0]+xn1-b1*xnbuffer1[1]+xnbuffer1[0]; 
    yn2=a1*ynbuffer2[1]-a2*ynbuffer2[0]+xn2-b1*xnbuffer2[1]+xnbuffer2[0]; 
    yn3=a1*ynbuffer3[1]-a2*ynbuffer3[0]+xn3-b1*xnbuffer3[1]+xnbuffer3[0];
    yn4=a1*ynbuffer4[1]-a2*ynbuffer4[0]+xn4-b1*xnbuffer4[1]+xnbuffer4[0];
    yn5=a1*ynbuffer5[1]-a2*ynbuffer5[0]+xn5-b1*xnbuffer5[1]+xnbuffer5[0];
    yn6=a1*ynbuffer6[1]-a2*ynbuffer6[0]+xn6-b1*xnbuffer6[1]+xnbuffer6[0];
    yn7=a1*ynbuffer7[1]-a2*ynbuffer7[0]+xn7-b1*xnbuffer7[1]+xnbuffer7[0];
    
    
    
    // sending the output of filter
    //blu.printf("%0.5f\r\n",yn1);
    
    //changing the values in the buffers for the next samples computation
    //1st channel
    ynbuffer1[0]=ynbuffer1[1];
    ynbuffer1[1]=yn1;
    xnbuffer1[0]=xnbuffer1[1];
    xnbuffer1[1]=xn1;
    //2nd channel
    ynbuffer2[0]=ynbuffer2[1];
    ynbuffer2[1]=yn2;
    xnbuffer2[0]=xnbuffer2[1];
    xnbuffer2[1]=xn2;
    //3rd channel
    ynbuffer3[0]=ynbuffer3[1];
    ynbuffer3[1]=yn3;
    xnbuffer3[0]=xnbuffer3[1];
    xnbuffer3[1]=xn3;
    //4th channel
    ynbuffer4[0]=ynbuffer4[1];
    ynbuffer4[1]=yn4;
    xnbuffer4[0]=xnbuffer4[1];
    xnbuffer4[1]=xn4;
    //5th channel
    ynbuffer5[0]=ynbuffer5[1];
    ynbuffer5[1]=yn5;
    xnbuffer5[0]=xnbuffer5[1];
    xnbuffer5[1]=xn5;
    //6th channel
    ynbuffer6[0]=ynbuffer6[1];
    ynbuffer6[1]=yn6;
    xnbuffer6[0]=xnbuffer6[1];
    xnbuffer6[1]=xn6;
    //7th channel
    ynbuffer7[0]=ynbuffer7[1];
    ynbuffer7[1]=yn7;
    xnbuffer7[0]=xnbuffer7[1];
    xnbuffer7[1]=xn7;
    
    //changing values for the x[n-1] buffer
    xn1prev=xn1now;
    xn2prev=xn2now;
    xn3prev=xn3now;
    xn4prev=xn4now;
    
        
    // amassing the outputs of the 7 notches to the corresponding 128-values buffers 
    if(i<128){
       chan1[i]=pow(yn1,2);
       chan2[i]=pow(yn2,2);
       chan3[i]=pow(yn3,2);
       chan4[i]=pow(yn4,2);
       chan5[i]=pow(yn5,2);
       chan6[i]=pow(yn6,2);
       chan7[i]=pow(yn7,2);
       i++;
                    }   
                    
     if(i==128){
        // rms computation           
        // with this for Σxi^2 is computed   for each channel  
           for(j=0;j<128;j++){
                 x[0]=x[0]+chan1[j];
                 x[1]=x[1]+chan2[j];
                 x[2]=x[2]+chan3[j];
                 x[3]=x[3]+chan4[j];
                 x[4]=x[4]+chan5[j];
                 x[5]=x[5]+chan6[j];
                 x[6]=x[6]+chan7[j];
                                    }
                // na mhn ksexasw na mhdenisw to x sto telos    
                  x[0]=sqrt(x[0]/128.0f);
                  x[1]=sqrt(x[1]/128.0f);
                  x[2]=sqrt(x[2]/128.0f);
                  x[3]=sqrt(x[3]/128.0f);
                  x[4]=sqrt(x[4]/128.0f);
                  x[5]=sqrt(x[5]/128.0f);
                  x[6]=sqrt(x[6]/128.0f);      
                  
                  blu.printf("%0.5f,%0.5f,%0.5f,%0.5f \r\n\0",x[0],x[1],x[2],x[3]);
                  
                  // re initialize x vector to zero 
                   for(j=0;j<7;j++){
                    x[j]=0;         }//for j end 
                                    
        i=0;
                    
                                     } // if i==128 end  
                                     }// if btn==1 end 
                                     
 interval=0;                                               
                    
                                     }// if interval ==1 end
        
        
        
        
        
        
        
        
        
        
    }// while true end
}// main end
   
