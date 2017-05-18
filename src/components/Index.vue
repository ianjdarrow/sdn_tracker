<template>
  <div class="container" id="content">
  <div class="row">
    <div class="eight columns">
      <div>
        <h2>SDN List Search</h2>
        <div v-if="loading" class="loader"><img src="../../static/squares.svg"></div>
      </div>
      <h3 v-if='error'>Error retrieving data</h3>
    </div>
    <div id="logoContainer" class="four columns">
    <img id="logo" src="../../static/lx.png" alt="LedgerX">
    </div>
  </div>
  <div class="row">
    <div class="eight columns">
      <input type='text' class="input" v-model="input" placeholder="Enter a name" :disabled="error || loading">
    </div>
    <div class="two columns checkboxes">
      <input type='checkbox' id='indCheckbox' v-model='showIndividuals'>
      <label for='indCheckbox'>Individuals</label>  
    </div>
    <div class="two columns checkboxes">
      <input type='checkbox' id='entityCheckbox' v-model='showEntities'>
      <label for='entityCheckbox'>Entities</label>
    </div>
  </div>
  <div v-if='!loading && !isInput' class="poke-div">
    <h3 class="poke-text">Start typing to filter results ({{sdnList.individuals.length + sdnList.entities.length}} total)</h3>
  </div>
  <div v-if='!loading && isInput'>
    <div id="ind-table" v-if='showIndividuals'>
      <h4>Individuals: {{ filteredIndividuals.length }}</h4>
      <table class="twelve columns">
        <thead v-if='filteredIndividuals.length > 0'>
          <tr>
            <th class="name-column">Name</th>
            <th class="info-column">Details</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="individual in filteredIndividuals">
            <td>{{ individual.lastName }}, {{ individual.firstName }}</td>
            <td>{{ individual.details }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div id="entity-table" v-if='showEntities'>
      <h4>Entities: {{ filteredEntities.length }}</h4>
      <table class="twelve columns">
        <thead v-if='filteredEntities.length > 0'>
          <tr>
            <th class="name-column">Entity Name</th>
            <th class="info-column">Details</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entity in filteredEntities">
            <td>{{ entity.name }}</td>
            <td>
              <ul>
                <li v-for="detail in entity.details">{{ detail }}</li>
              </ul>
            </td>
          </tr>
        </tbody>
      </table>
      </div>
      <div class="row">
      </div>
    </div>
    <div class="twelve columns footer">
      <p>Made by <a href="mailto:ian@ledgerx.com">Ian</a> in 2017 (<a href="https://github.com/ianjdarrow/sdn_tracker">Github</a>)</p>
    </div>
  </div>
</template>

<script>

import debounce from 'debounce'

export default {
  name: 'index',
  data () {
    return {
      msg: 'LedgerX SDN Checker',
      sdnList: {
        individuals: [],
        entities: []
      },
      showIndividuals: true,
      showEntities: true,
      input: '',
      search: '',
      error: false,
      loading: true,
    }
  },
  watch: {
    input: function() {
      this.updateSearch();
    }
  },
  methods: {
    getSDNList: function() {
      this.$http.get('http://localhost:5000/list').then(response => {
        this.sdnList.individuals = response.body.individuals;
        this.sdnList.entities = response.body.entities;
        this.loading = false;
        }, response => {
          this.error = true;
          this.loading = false;
        }
      );
    },
    updateSearch: debounce(function () {
      this.search = this.input;
    }, 200),
  },
  computed: {
    filteredIndividuals: function() {
      return this.sdnList.individuals.filter(individual => {
        return individual.lastName.indexOf(this.search.toUpperCase()) > -1
      });
    }, 
    filteredEntities: function() {
      return this.sdnList.entities.filter(entity => {
        return entity.name.indexOf(this.search.toUpperCase()) > -1
      });
    }, 
    isInput: function() {
      return (this.search.length > 1);
    },
  },
  created: function() {
    this.getSDNList();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

th, td {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
tr {
  min-height: 25px;
  vertical-align: top;
  line-height: 1.35em;
}
label {
  display: inline-block;
}
li {
  list-style-type: none;
}
input {
  border-radius: 0;
}
#content {
  min-height: 90vh;
}
#logoContainer {
    height: 60px;  
    align-items: flex-end;
    display: flex;
    flex-direction: column;
}
#logo {
  margin-top: 10px;
  align-self: flex-end;
}
.loader {
  position: absolute;
  top: -8px;
  left: 300px;
}
.input {
  width: 100%;
  height: 50px;
  font-size: 1.5em;
  border: 0px;
  border-bottom: 2px solid #aaa;
}
.input:focus {
  border: 0px;
  border-bottom: 2px solid #47b;
}
.checkboxes {
  padding-top: 30px;
  text-align: right;
  /*border: 2px solid #33f;*/
  height: 50px;
}
.checkboxes.selected {
  /*background: #fdf;*/
}
.poke-div {
  padding-top: 200px;
}
.poke-text {
  color: #aaa;
  font-style: italic;
  text-align: center;
}
.name-column {
  width: 33%;
}
.info-column {
  width: 67%;
}
.footer {
  text-align: center;
  font-weight: lighter;
  color: #aaa;
  height:60px;
  position: absolute;
  bottom: 0;
  padding-top: 60px;
}

</style>
