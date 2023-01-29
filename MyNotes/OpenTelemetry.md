# Open Telemetry

<b>Components</b>
OpenTelemetry can be further divided into other logical components that comprise the typical OTel solution. They are 
<ol>
<li><b>APIs</b>: In charge of gathering the telemetry and all the data that is part of it </li>
<li><b>SDKs</b>: get this data out of the current observed process to another entity for analysis</li>
<li><b>Collector</b>: Send this data to destination</li>
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

<b>Three Pillars of Observability</b><br>
Types of data</br>
<ul>
<li><b>Logs:</b> Immutable, timestamped record of discrete events that happened over time</li>
<li><b>Metrics:</b> numeric representation of data measured over intervals of time</li>
<li><b>Traces:</b>representation of a series of causally related distributed events that encode the end-to-end request flow through a distributed system</li>
</ul>

<b>Instrumentation</b><br>
 “Instrumentation” referring to the act of collecting trace data. 2 ways to instrument the code
 <ul>
 <li>Manual: Explicitly telling our software what data to expose</li>
 <li>Automation: A way to instrument your application without touching your source code.</li>
 </ul>

<b>Automatic Instrumentation</b> will give you a similar out of the box experience. If you previously used an APM agent to extract telemetry from your application<br>
<b>Manually instrument</b> your applications by coding against the OpenTelemetry APIs.<br>
<b>Steps:</b>
<ul>
<li>Import the OpenTelemetry API and SDK </li>
<li>Configure the OpenTelemetry API</li>
<li>Configure the OpenTelemetry SDK </li>
<li>Create Telemetry Data</li>
<li>Export Data</li>
</ul>

A trace includes one or more spans, which are the instances of a particular operation. A span has a parent span that it is linked to, unless it is the first span in the trace in which case its span parent ID is all zeros.<br>

<image src="trace.jpg">

The way that we can add spans to an existing trace (or start a new one) is through the API module.<br>
Include OTel Module and create a span by making a call to the global tracer provider <br>

Example for Go Application:
<pre>
import "go.opentelemetry.io/otel"

// ... other code ...

ctx, span := otel.Tracer("my-telemetry-library").Start(r.Context(), "get_user_cart")
defer span.End()
</pre>
