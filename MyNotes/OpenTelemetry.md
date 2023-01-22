# Open Telemetry

<b>Components</b>
OpenTelemetry can be further divided into other logical components that comprise the typical OTel solution. They are 
<ol>
<li>APIs: In charge of gathering the telemetry and all the data that is part of it </li>
<li>SDKs: get this data out of the current observed process to another entity for analysis</li>
<li>Collector: Send this data to destination</li>
</ol>


Because they are separate, they allow us to decouple <b>what is observed</b> (API) to <b>how it is handled</b> (SDK). </br>

The collector’s entire job can be broken down into three different stages:<br>
<ol>
<li>Receive telemetry data</li>
<li>Process telemetry data</li>
<li>Export telemetry data</li>
</ol>
The collector is an ETL pipeline for telemetry data.<br>
<hr>