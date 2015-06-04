# Introduction

- Architect for change
    - to the extent that one can make change less expensive, it enables the to evolve over time
- Separate Goals from Approaches
- Architecture isn't an equation to be solved; it's a snapshot of a process.
- Architecture is coupled to process (especially continuous delivery).


## Agenda

- 3 kinds of architecture
    - application architecture
    - integration architecture
    - enterprise architecture

- Cross cutting skills
    - soft skills
    - continuous delivery
    - understanding large codebases

- application architecture
    - techniques for change
    - patterns and anti-patterns
    - tools & documentation

- integration architecture
    - overview
    - architectural styles specific to integration architecture

- enterprise architecture
    - intro to enterprise architecture


# Architecture Soft Skills Part 1

- the choice of technology should never drive the architecture
    - in fact, it should be the other way around
    - anti-pattern: e.g. an org pick products, then attempts to build an arch around those products

## Expectations of the Architect

1. analyze technology, industry and market trends and keep current with those latest trends.
1. analyze the current technology environment and recommend solutions for improvement.
1. ensure compliance with the architecture
    - this is the herding cats task
1. have exposure to multiple and diverse technologies, platforms, and environments.
1. possess exceptional interpersonal skills, including teamwork, facilitation, and negotiation.
1. define the architectures and design principles to guide technology decisions for the enterprise.
1. understand the politial climate of the enterprise and be able to navigate the politics.
    - rule of thumb: in negotiation: never ask a question you don't know the answer to.  Don't get surpised in public

## Achitecture Aspects or Soft Skills

- leadership and communication
- technical knowledge
- business domain knowledge
- methodology and strategy

# Continuous Delivery

Definition of Continuous Integration:

> Fast, automated feedback on the correctness of your application every time
there is a change to code.

Definition of Continuous Delivery:

> Fast, automated feedback on the production readiness of your application every
time there is a change -- to code, infrastructure, or configuration.

## Continuous Delivery Ideal

- software is always production ready
- deployments are reliable and commonplace
- everyone can self-service deployments
- releases occur according to business needs, not operational constraints

### Prerequisites

- extensive configuration management
- excellent automated testing at multiple levels
- continuous integration

## Commit stage

- compile
- unit test
- assemble
- code analysis

- run against each check-in (continuous integration)
- fix immediately upon failure
- converts version controlled assets into binaries used in subsequent stages

## Acceptance Stage

- configure environment
- deploy and smoke test
- acceptance test
- tear down

- end-to-end tests in a production-like environment
- triggered by upstream success
- fix immediately upon failure

## Manual Stage

- UAT, staging, integration, production
- manual processes need to be pull-based, not push-based
    - no jelly views
- deployments self service (push button)

the ultimate goal of continuous delivery is to reduce cycle time: the amount of time
between when work starts on a feature to when it is available to customers.

## Production-like

Nothing here is dogmatic; driven by goals.  Flexibility.

The first step in the process is "Configure environment".  What does this mean?

- the goal: increasing confidence in build's production readiness; over time
- so: the "environment" becomes more production-like over time
- this should result in: faster feedback to developers

"Chicken counting": supposedly a chicken can only distinguish: 0, 1 or many.
So anything that is quantity 2 or more == 2.

so max out at 2.

## Principles of Software Delivery

- create a repeatable, reliable process for releasing software

### How to achieve?

- automate almost everything
    - build
    - deploy
    - test
    - release
- but leave high value manual tasks manual
    - manual testing
    - approvals

- mantra: separate automatable from high-value humans only work.

## Version Control

mantra: keep everything you need to build, deploy, test and release in version control

- requirements docs
- test scripts
- automated test cases
- network config scripts
- technical documentation
- database creation, manipulation & initialization scripts
- application scripts
- libraries
- tool chains

idea: use puppet / chef to spin up a developer image.

cool tool: github boxen

the book: _Continuous Delivery_ Jez Humble, David Farley

# Architecture Soft Skills Part 2

## Architecture Soft Skills

- leadership and communication
- technical knowledge
- business domain knowledge
- methodology and strategy


## Leadership and Communication

The 3 C's:

- communication
- collaboration


### Communication

- effectively communicate ideas, concepts, issues and solutions to stakeholders

- what is a stakeholder?
    - developer
    - tester
    - CIO
    - basically, anyone with a vested interest in the business system


### Collaboration

- get stakeholders involved in the architecture process and *solicit* ideas and
feedback early and often

### Clarity

- articulate the architecture solution in clear and concise terms as appropriate
to each stakeholder

### Translation Skills

- flexibility
- agility
- feasibility

## Technical Knowledge

the triangle of knowledge:

- stuff you know (at the top)
- stuff you know you don't know
- stuff you don't know that you don't know

so the game is to move stuff up the triangle

as an architect technical breadth (stuff you know you don't know) is more
important than technical depth (stuff you know).

So focus on stuff you know you don't know.

### multi-platform knowledge

avoid the "golden hammer anti-pattern"

InfoQ as a source of information to build breadth.

## Business Domain Knowledge

how important is it that an architect understand the business?  A: important

Why knowing the business is critical

- communicate better with the business
- better understand business goals, issues and trends
- gain trust by speaking the business language
- design the system to better handle future changes
- better determine the correct architecture patterns

## Methodology and Strategy

key point: once we know where we want to go, how do we get there?

- Continuous delivery is one tool

- scrum
- lead
- feature driven development
- even waterfall

### Hybrids

## References

- _97 Things Every Software Architect Should Know_, Monson-Haefel et.al, O'Reilly
- _A Practical Guide to Enterprise Architecture_, McGovern et.al, PTR  Prentiss
- _Software Architecture in Practice 3rd Edition_, Bass et.al, Addison Wesley

## Understanding Large Codebases

- micro <-> macro

### Metrics

- we would like the metrics to be nice and deterministic
    - but that is not the reality
    - much softer and fuzzier

#### Cyclomatic complexity

- function or method level metric
    - provides a numeric value representing the complexity of a function or method

#### Chidamber & Kemerer OO metrics

- Authors:
    - Shyam R Chidamber
    - Chris F. Kemerer
- [paper](http://faculty.salisbury.edu/~stlauterburg/cosc425/metricforood_chidamberkemerer94.pdf)
- bundles prior metrics is a way that works well in OO.

##### Easy C&K metrics

- DIT: depth of inheritance tree
- NOC: number of children
- NPM: number of public methods

##### Quite Useful C&K metrics

- WMC: weighted methods per class: ∑ of cyclomatic complexity.
- RFC: response for class: # of methods executed due to a method call
- LCOM: lack of cohesion: ∑ of sets of methods not shared via sharing fields
    - attempts to display whether methods are operating on common fields.
    - a higher score may indicate that futher factoring of the class may be warranted.

these next two may be the most useful from architecture standpoint, because they indicate coupling.

- CE: efferent coupling: ∑ of other classes this class uses (outgoing calls)
- CA: afferent coupling: ∑ of how many other classes use this class (incoming calls)

if cyclomatic complexity is a measure of complexity, then afferent coupling is a measure
of importance.

##### Kiviat Metrics or Kiviat Graphs

- freeware (win-tel binary) metric generator [source monitor](http://www.campwoodsw.com/sourcemonitor.html)

- for Kiviat graphs, you are looking for:
    - asymmetries
    - outliers

##### Heat Maps

- open source [panopticode](http://sourceforge.net/projects/panopticode/)
    - last updated in 2007
    - wiki page last updated 2013-04

- looking for:
    - hot-spots
    - clusters

##### Size and Complexity Pyramid

- [commercial tool](http://www.intooitus.com/products/incode)

##### Visualizations

- Erik Doernenburg [site](http://erik.doernenburg.com/)
    - [Toxicity charts](http://erik.doernenburg.com/2013/06/toxicity-reloaded/)
- for java, [checkstyle](http://checkstyle.sourceforge.net/) is the static source code tool they use

in the smalltalk world:

- code crawler
- moose
    - you can take a java code base, and generate
- these may be historically interesting

back to Java:

- [x-ray](http://xray.inf.usi.ch/xray.php)
- jdepend gives some of those proximity metrics that x-ray gives as well.

code complexity

code city

### Metrics Limitations

- signal to noise ratio
- no "1 True Metric"
    - need a combination of metrics
    - so an exploration of metrics is likely needed
- gathered but ignored
- inaction and/or overaction
    - the "Hawthorn Effect".  a 1920s experiment.
        - visual: does lighting affect worker productivity?
- prefer trends to discrete value
    - so you have to monitor over time
    - e.g. is cyclomatic complexity of 12 good or bad?
        - but 12 -> 20 -> 35 is an indicator of something to watch.
    - [SonarQube](http://www.sonarqube.org/) is a nice visualization tool that shows trends.

### uses for metrics

- information radiators
    - wire something into the build to publish data to a dashboard
- probes
    - investigation driven

## Architecting for change

Architecture agility
: the ability to respond *quickly* to a constanntly changing environment

### Techniques for Change

- there are trade-offs here

#### Reduce Dependencies

- We have a lot of tooling to understand dependencies.  So we want to get to looser coupling; whether that is by messaging, or ...
- contract changes usually are pervasive.

- components can evolve independently

##### trade-offs for dependency reduction

- abstraction for decoupling adds a layer
    - so performance may be affected

##### implementation

could be done via:

- messaging
- a service bus
- adapters
- architecture patterns


#### Leverage Standards

3 types of standards that can be leveraged:

- industry standards
    - e.g.:
        - swift
        - soap
        - xml
        - fix protocol
        - FpML
- corporate standards
    - e.g.:
        - .net
        - j2ee
        - rails
        - Eclipse
    - we use these to achieve economies of scale in the workforce.
        - a java shop is not likely to have a large pool of rails developers.
- defacto standards
    - e.g.:
        - hibernate
        - spring
        - struts
        - tomcat

- a given standard may not be your first choice, but they do significantly reduce the
effort to achieve a given change; you can count on a larger pool of talent, and thus do
not have to educate your workforce before they can even begin work.
- and leveraging standards typically helps reduce system integration issues

#### Create Product-agnostic Architectures

goal
: isolate products to avoid vendor lock-in

Use:

- messaging
- adapters
- architecture patterns

#### Create Domain-specific Architectures

- generic architectures -- aka *infinity architectures* -- are difficult to change
because they are too broad adn take into account scenarios that are not actually used.
- the mitigation technique is: limit the scope of the architecture by taking into
account drivers, requirements, business direction and industry trends.
- Combine these 4 concerns:
    - business requirements
    - business goals
    - business direction
    - industry trend
- to arrive at the domain specific architecture.

## Architecture Patterns Part 1

### History of Patterns Movement

### Traditional Layered Architecture

- often the layers are *closed*; i.e., there is no reaching around a layer
to get to the one underneath it; you have to go through each layer.

#### Advantages

- separation of concerns
- layers of isolation

