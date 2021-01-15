int forw = 2;

int lef = 3;

int rsp = 4;
  int forwl;
  int lefl;
  int rspl;


void setup() {
Serial.begin(9600);
  // put your setup code here, to run once:
pinMode(forw,INPUT);

pinMode(lef,INPUT);

pinMode(rsp,INPUT);

}

void loop() {
radio();

if (forwl<1200 and lefl>1600){
  Serial.write("rst");
  
}
else if(forwl>1600 and lefl>1600){
 Serial.write("rsd"); 
 
}
else if(forwl<1200 and lefl<1200){
  Serial.write("lst");
}
else if(forwl>1600 and lefl<1200){
  Serial.write("lsd");
}
else if(forwl<1200){
  Serial.write("for");
}
else if(forwl>1600){
  Serial.write("bac");
}
else if(lefl<1200){
  Serial.write("lef");
}
else if(lefl>1600){
  Serial.write("rig");
  
}
else if(rspl>1600){
  Serial.write("rsp");
 
 
}
else if(rspl<1200){
  Serial.write("lsp");

}
else{
  Serial.write("sto");
  
}

}
void radio(){

 forwl = pulseIn(forw,HIGH,60000);
 lefl = pulseIn(lef,HIGH,60000);
 rspl = pulseIn(rsp,HIGH,60000);
//Serial.print("forw");  
//Serial.print(forwl); 
//Serial.print("  ");

//Serial.print("lef");
//Serial.print(lefl);
//Serial.print("  ");

//Serial.print("rsp");
//Serial.print(rspl);
//Serial.println("  ");
}
